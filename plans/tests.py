from django.test import TestCase
from collections import OrderedDict
import pytest
from .models import Plans,AvilableExcercises,Musclesgroup,Traninglog, PlanName
from django import urls
from accounts.models import CustomUser
def test_it_works():pass

#path("plans/",views.UsersPlansList.as_view(), name="preview"), done
   # path("addplan/",views.PlansLookupAndCreatePlans.as_view(), name="PlansLookupAndCreatePlans"), done
  #  path("excercises/",views.AllExcercisesLookup.as_view(), name="AllExcercisesLookup"), done
 #   path("recordresults/",views.RecordTraningResults, name="record"), done
#    path("delete/<int:id>",views.DelatePlanAPI.as_view(), name="DelatePlanAPI"), done
plandata={
    "planname": "plan1",
    "excercise": "Cwiczenie",
    "owner": 1
}

# Create your tests here.
@pytest.mark.django_db
@pytest.fixture(scope='session')
def created_user(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return CustomUser.objects.create_user(username="User", password="UserPassword",email="teest@test.com")


@pytest.mark.django_db
@pytest.fixture(scope='session',)
def create_excercise(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        MusclesgroupInstance = Musclesgroup(name="plecy")
        MusclesgroupInstance.save()
        excerciseInstance=AvilableExcercises(name="Cwiczenie",musclesgroup=MusclesgroupInstance)
        return excerciseInstance.save()

@pytest.mark.django_db
@pytest.fixture()
def login_token(created_user,client):
    login_data={"username":created_user.username,"email":created_user.email,"password":"UserPassword"}
    login_url=urls.reverse("rest_login")
    print(created_user.username)
    print(created_user.email)
    print(created_user.password)
    response=client.post(login_url,login_data)
    return response.data['key']


@pytest.mark.django_db
@pytest.fixture(scope='session',)
def create_Plan(django_db_setup, django_db_blocker,created_user):
    with django_db_blocker.unblock():
        #MusclesgroupInstance = Musclesgroup(name="plecy")
        #MusclesgroupInstance.save()
        #excerciseInstance=AvilableExcercises(name="Cwiczenie",musclesgroup=MusclesgroupInstance)
        #excerciseInstance.save()
        PlanName_instance=PlanName(name="plan1",owner=created_user)
        PlanName_instance.save()
        Plan_instance=Plans(planname=PlanName.objects.get(id=1),excercise=AvilableExcercises.objects.get(id=1),owner=created_user)
        return Plan_instance.save()


@pytest.mark.django_db
def test_UsersPlansList_model():
    assert Plans.objects.count()==0


@pytest.mark.django_db
def test_create_user(created_user):
    user=created_user
    assert user!=None
    assert CustomUser.objects.count()==1
    assert user.username=="User"


@pytest.mark.django_db
def test_create_excercise(create_excercise):
    assert Musclesgroup.objects.count()==1
    assert AvilableExcercises.objects.count() == 1
    assert AvilableExcercises.objects.get(id=1).name=="cwiczenie"


@pytest.mark.django_db
def test_create_plan(client,create_excercise,login_token,create_Plan):
    create_plan_url=urls.reverse("PlansLookupAndCreatePlans")
    resp = client.post(create_plan_url,data=plandata,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code == 201
    assert resp.data=={'id': 2, 'planname': 'plan1', 'excercise': 'cwiczenie', 'owner': 1}


@pytest.mark.django_db
def test_create_delate_view_plan(client,create_excercise,created_user,login_token):
    user=created_user
    create_plan_url=urls.reverse("PlansLookupAndCreatePlans")
    resp=client.post(create_plan_url,data=plandata,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code==201
    assert resp.data=={'id': 2, 'planname': 'plan1', 'excercise': 'cwiczenie', 'owner': 1}
    look_for_unique_plans = urls.reverse("preview")
    resp=client.get(look_for_unique_plans,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code==200
    assert resp.data==[{"name":"plan1","id":1}]
    look_for_excercises_in_plan=urls.reverse("PreviewExercisesOnPlan",args=[1,])
    resp=client.get(look_for_excercises_in_plan,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code==200
    assert resp.data==[OrderedDict([('id', 1), ('excercise', 'cwiczenie'), ('planname', 'plan1')]), OrderedDict([('id', 2), ('excercise', 'cwiczenie'), ('planname', 'plan1')])]
    print(resp.data)

    delete_plan_url = urls.reverse("DelatePlanAPI", args=[1, ])
    resp=client.delete(delete_plan_url,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code == 204
    assert resp.data ==None
    resp = client.get(look_for_excercises_in_plan, HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code == 200
    assert resp.data == [OrderedDict([('id', 2), ('excercise', 'cwiczenie'), ('planname', 'plan1')])]
    delete_planname_url=urls.reverse("DelatePlanNameAPI",args=[1,])
    resp=client.delete(delete_planname_url,HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code == 204
    resp = client.get(look_for_excercises_in_plan, HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code == 200
    assert resp.data==[]

@pytest.mark.django_db
def test_create_training_log(client,create_Plan,created_user,login_token):

    assert Musclesgroup.objects.count()==1
    assert AvilableExcercises.objects.count() == 1
    assert AvilableExcercises.objects.get(id=1).name=="cwiczenie"
    assert Plans.objects.count()==1
    record_training_url = urls.reverse("record")
    resp = client.post(record_training_url,data={
        "excercise": "cwiczenie",
        "reps": 1,
        "weight": 2.0,
        "date": "2023-03-20"
    }, HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code==200
    assert resp.data==[{
        "id":1,
        "excercise": "cwiczenie",
        "reps": 1,
        "weight": 2.0,
        "date": "2023-03-20"
    }]
@pytest.mark.django_db
def test_All_excercises_lookup(client,create_Plan,created_user,login_token):

    assert Musclesgroup.objects.count()==1
    assert AvilableExcercises.objects.count() == 1
    assert AvilableExcercises.objects.count() == 1
    assert AvilableExcercises.objects.get(id=1).name=="cwiczenie"
    assert Plans.objects.count()==1
    ExcercisesLookup = urls.reverse("AllExcercisesLookup")
    resp = client.get(ExcercisesLookup, HTTP_AUTHORIZATION=f"Token {login_token}")
    assert resp.status_code==200
    assert resp.data==[OrderedDict({"name":"cwiczenie","musclesgroup":"plecy"})]
