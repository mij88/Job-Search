# Job Search Record Project

A Project to allow users to record  and edit jobs that they have applied 

#### Installation

```bash
git clone https://github.com/mij88/Job-Search.git

cd Job-Search

cd backend
```

### Dependancies

With macOS replace pip with pip3

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install flask-cors
```

### Run Program

Must be in backend directory

```bash
python main.py
```
### Testing

Testing API endpoints using Postman

#### 1. Testing Get Jobs
No jobs are added yet but job list is displayed

![alt text](/images/1.png)

#### 2. Testing Add Job
Adding new job for Apple

![alt text](/images/2.png)

New Job is shown using get jobs!

![alt text](/images/3.png)

#### 3. Testing Update Job

Updating postion and additionalInfo

![alt text](/images/4.png)

Positon and additionalInfo has been updated!

![alt text](/images/5.png)

#### 4. Testing Delete Job

Adding new job for Google

![alt text](/images/6.png)

New Job is added!

![alt text](/images/7.png)

Now deleting first job with Apple

![alt text](/images/8.png)

First job with Apple deleted and only Google job is left!

![alt text](/images/9.png)
