from models import Role


def make_db_seed(db):
    print("== Seeding database")
    db.session.begin(subtransactions=True)
    try:
        seed_roles(db)
    except:  # noqa: E722
        db.session.rollback()
        raise


def seed_roles(db):
    print("++ Seeding roles")
    role_usr = Role()
    role_usr.name = "user"
    role_usr.description = "Simple user"

    role_adm = Role()
    role_adm.name = "admin"
    role_adm.description = "Admin user"

    db.session.add(role_usr)
    db.session.add(role_adm)
    db.session.commit()
    db.session.commit()
    # two commit because wtf ?
