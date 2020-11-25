import csv
from flask.cli import FlaskGroup
from project import app, db, User, Biocontainers

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="test@test.org"))
    db.session.commit()
    f = open("biocontainers.csv", encoding="utf-8")
    #to skip header line
    reader = csv.reader(f)
    next(reader,None)
    for name, version, category, keywords, description, url, moduleName in reader:
        db.session.execute("INSERT INTO biocontainers (name, version, category, keywords, description, url, moduleName) VALUES (:name, :version, :category, :keywords, :description, :url, :moduleName)",
                    {"name":name, "version":version, "category":category, "keywords":keywords, "description":description, "url":url, "moduleName":moduleName})
        print(f"Adding data into biocontainers table")
    db.session.commit()

if __name__ == "__main__":
    cli()
