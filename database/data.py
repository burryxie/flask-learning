import os
import pprint
from sqlalchemy import create_engine, text, insert

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)



def load_recent_3jobs_from_db():
    sql_string = """
        select 
            id ,department ,title ,salary ,location
            ,case when if_part_time=1 then '兼职' else '全职' end as if_part_time
            ,education_requirement ,experience_requirement ,skill_requirement
            ,job_description ,job_pic_url
        from job_details 
        order by updated_time desc 
        limit 3
    """
    with engine.connect() as conn:
        result = conn.execute(text(sql_string))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs


def load_all_jobs_from_db():
    sql_string = """
        select 
            id ,department ,title ,salary ,location
            ,case when if_part_time=1 then '兼职' else '全职' end as if_part_time
            ,education_requirement ,experience_requirement ,skill_requirement
            ,job_description ,job_pic_url
        from job_details 
        order by updated_time desc 
    """
    with engine.connect() as conn:
        result = conn.execute(text(sql_string))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs



def load_job_detail_from_db(id):
    sql_string = """
        select 
            id ,department ,title ,salary ,location
            ,case when if_part_time=1 then '兼职' else '全职' end as if_part_time
            ,education_requirement ,experience_requirement ,skill_requirement
            ,job_description ,job_pic_url
        from job_details 
        where id=
    """+str(id)
    with engine.connect() as conn:
        result = conn.execute(text(sql_string))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs


def add_application_to_db(data):
  with engine.connect() as conn:
    query = text("""
                 INSERT INTO job_apply_details 
                      (name, age, gender, phone, email, comment, job_id, job_title, department, location, resume_url) 
                 VALUES 
                      ('{name}', {age}, '{gender}', {phone}, '{email}', '{message}', {job_id}, '{job_title}', '{department}', '{location}', '{resume_file}') 
                """.format(**data))
    # print(query)
    conn.execute(query)
