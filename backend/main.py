from flask import request, jsonify # return json data
from config import app, db
from job_model import Job

@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()
    json_jobs = list(map(lambda x: x.to_json(), jobs)) #apply to to_json() to every item in jobs list
    return jsonify({"jobs": json_jobs})

@app.route("/add_job", methods=["POST"])
def add_job():
    company_name = request.json.get("companyName")
    position = request.json.get("position")
    job_link = request.json.get("jobLink")
    date_applied = request.json.get("dateApplied")
    additional_info = request.json.get("additionalInfo")

    if not company_name or not position or not date_applied:
        return (
            jsonify({"message": "You are missing either company name, position or date applied"}), 
            400,
        )

    new_job = Job(company_name=company_name, 
                  position=position, 
                  job_link=job_link, 
                  date_applied=date_applied,
                  additional_info=additional_info)
    
    try:
        db.session.add(new_job) #add but not fully commited
        db.session.commit() #permanantly commit adding job

    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Job recorded"}), 201 #if no error occurs then send this message to user


@app.route("/update_job/<int:job_id>", methods=["Patch"])
def update_job(job_id):
    job = Job.query.get(job_id)

    if not job:
        return jsonify({"message": "Job with id of " + str(job_id) + " not found"}), 404
    
    data = request.json
    job.company_name = data.get("companyName", job.company_name) #modify job to update company name (if no company name found then leave as is)
    job.position = data.get("position", job.position)
    job.job_link = data.get("jobLink", job.job_link)
    job.date_applied = data.get("dateApplied", job.date_applied)
    job.additional_info = data.get("additionalInfo", job.additional_info)

    db.session.commit()

    message = "Job with id " + str(job_id) + " updated"

    return jsonify({"message": "Job with id: " + str(job_id) + " updated"}), 200

@app.route("/delete_job/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = Job.query.get(job_id)
 
    if not job:
        return jsonify({"message": "Job with id of " + str(job_id) + " not found"}), 404
    
    db.session.delete(job) ## delete job
    db.session.commit()

    return jsonify({"message": "Job with id of " + str(job_id) + " deleted"}), 200

if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all() #spin up database

    app.run(debug=True) #only run this code if the main.py is run directly (dont run if main.py is imported)
