import pytest


@pytest.fixture()
def customer_profile(db_connection, faker):
    email = faker.safe_email()
    yield {"firstname": faker.first_name(),
           "lastname": faker.last_name(),
           "email": email,
           "phone": str(faker.random_number(digits=9, fix_len=True)),
           "password": faker.safe_email(),
           }

    # delete from database
    query = "DELETE FROM oc_customer WHERE email=%s"
    db_connection.cursor().execute(query, (email,))
    db_connection.commit()
