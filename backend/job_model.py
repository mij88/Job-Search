from config import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(800), unique =False, nullable=False)
    position = db.Column(db.String(800), unique =False, nullable=False)
    job_link = db.Column(db.String(800), unique =True, nullable=False)
    date_applied = db.Column(db.String(100), unique =True, nullable=False)
    additional_info = db.Column(db.String(800), unique =True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "position": self.position,
            "job_link": self.job_link,
            "date_applied": self.date_applied,
             "additional_info" : self.additional_info

        }