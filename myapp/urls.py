from django.urls import path
from . import views

urlpatterns=[
    path("home",views.home),
    path("adminportal",views.adminportal),
    path("regg",views.regg),
    path("admin",views.admin),
    path("view",views.view),
    path("login",views.login),
    path("courses",views.courses),
    path("courseview",views.courseview),
    path("courseview2",views.courseview2),
    path("sub",views.sub),
    path("subview",views.subview),
    path("addpaper",views.addpaper),
    path("paperview",views.paperview),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),
    path("editsub/<int:id>",views.editsub),
    path("updatesub/<int:id>",views.updatesub),
    path("deletesub/<int:id>",views.deletesub),
    path("viewpaper",views.viewpaper),
    path("exam",views.exam),
    path("result",views.result),
    path("examresult",views.examresult),
    path("viewresult",views.viewresult),
    path("sturesult/<str:name>",views.sturesult),
    # path("get_subjects_by_course",views.get_subjects_by_course),

    path('c/<int:course_id>/<int:id>',views.coursesub)
]
