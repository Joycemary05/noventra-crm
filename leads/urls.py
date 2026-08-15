from django.urls import path
from . import views

urlpatterns = [

    # Authentication
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Leads
    path("leads/", views.leads_list, name="leads_list"),
    path("leads/add/", views.add_lead, name="add_lead"),
    path("leads/import/", views.import_excel, name="import_excel"),
    path("leads/export/", views.export_excel, name="export_excel"),
    path("leads/<int:lead_id>/", views.lead_detail, name="lead_detail"),
    path("leads/<int:lead_id>/edit/", views.edit_lead, name="edit_lead"),
    path("leads/<int:lead_id>/delete/", views.delete_lead, name="delete_lead"),

    # Follow-ups
    path(
        "leads/<int:lead_id>/followup/",
        views.add_followup,
        name="add_followup",
    ),
]