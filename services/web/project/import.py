# script rewritten in ./manage.py, current file can be used as a reference
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    biocontainers_table = "CREATE TABLE IF NOT EXISTS biocontainers (tool_id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, version VARCHAR NOT NULL, category VARCHAR NOT NULL, keywords VARCHAR NOT NULL, description VARCHAR NOT NULL, url VARCHAR NOT NULL, moduleName VARCHAR NOT NULL)"
    db.execute(biocontainers_table)
    db.commit()
    print(f"Created biocontainers table if it did not exist earlier")
    # to import data into the biocontainers table
    f = open("biocontainers.csv")
    #to skip header line
    reader = csv.reader(f)
    next(reader,None)
    for name, version, category, keywords, description, url, moduleName in reader:
        db.execute("INSERT INTO biocontainers (name, version, category, keywords, description, url, moduleName) VALUES (:name, :version, :category, :keywords, :description, :url, :moduleName)",
                    {"name":name, "version":version, "category":category, "keywords":keywords, "description":description, "url":url, "moduleName":moduleName})
        print(f"Adding data into biocontainers table")
    db.commit()

if __name__ == "__main__":
    main()
