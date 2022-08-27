mkdir -p extra/pylint-reports

# Pylint
pylint src/clean_architecture_django/ > extra/pylint-reports/pylint-report-clean_architecture_django.txt
pylint src/common_library/ > extra/pylint-reports/pylint-report-common_library.txt
pylint src/local_services/ > extra/pylint-reports/pylint-report-local_services.txt
pylint src/external_services/ > extra/pylint-reports/pylint-report-external_services.txt
pylint src/default_app/ > extra/pylint-reports/pylint-report-default_app.txt
