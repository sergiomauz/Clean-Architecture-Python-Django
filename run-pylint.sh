mkdir -p extra/pylint-reports

# Pylint
pylint clean_architecture_django/ > extra/pylint-reports/pylint-report-clean_architecture_django.txt
pylint common_library/ > extra/pylint-reports/pylint-report-common_library.txt
pylint local_services/ > extra/pylint-reports/pylint-report-local_services.txt
pylint external_services/ > extra/pylint-reports/pylint-report-external_services.txt
pylint default_app/ > extra/pylint-reports/pylint-report-default_app.txt
