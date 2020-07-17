import psycopg2

con = psycopg2.connect(
            host = "174.138.126.45",
            database = "unireview",
            user = "postgres",
            password = "kUbhREPunaMyAVVAv5uc",
            port = 5432,)

cur = con.cursor()

cur.execute("insert into unireview_app_course (university, course_code, university_id, course_title, average_score) values (%s, %s, %s, %s, %s)")

cur.execute("select * from unireview_app_course")

rows = cur.fetchall()

for r in rows:
    print(r)

con.commit()

cur.close()

con.close()

