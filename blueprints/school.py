from flask import Blueprint,request,jsonify
from models.schools import School
from extentions.db_extension import Session
import uuid
from services.province_service import ProvinceService
school_bp = Blueprint('school',__name__)
    
dummy_schools = [
    {
        'name': 'School 1',
        'email': 'school1@example.com',
        'total_rooms': 50,
        'province': 'California'
    },
    {
        'name': 'School 2',
        'email': 'school2@example.com',
        'total_rooms': 30,
        'province': 'New York'
    },
    {
        'name': 'School 3',
        'email': 'school3@example.com',
        'total_rooms': 40,
        'province': 'Texas'
    },
    {
        'name': 'School 4',
        'email': 'school4@example.com',
        'total_rooms': 60,
        'province': 'Florida'
    },
    {
        'name': 'School 5',
        'email': 'school5@example.com',
        'total_rooms': 25,
        'province': 'Illinois'
    },
    {
        'name': 'School 6',
        'email': 'school6@example.com',
        'total_rooms': 35,
        'province': 'Pennsylvania'
    },
    {
        'name': 'School 7',
        'email': 'school7@example.com',
        'total_rooms': 45,
        'province': 'Ohio'
    },
    {
        'name': 'School 8',
        'email': 'school8@example.com',
        'total_rooms': 55,
        'province': 'Georgia'
    },
    {
        'name': 'School 9',
        'email': 'school9@example.com',
        'total_rooms': 70,
        'province': 'North Carolina'
    },
    {
        'name': 'School 10',
        'email': 'school10@example.com',
        'total_rooms': 20,
        'province': 'Michigan'
    },
    {
        'name': 'School 11',
        'email': 'school11@example.com',
        'total_rooms': 80,
        'province': 'California'
    },
    {
        'name': 'School 12',
        'email': 'school12@example.com',
        'total_rooms': 90,
        'province': 'New York'
    },
    {
        'name': 'School 13',
        'email': 'school13@example.com',
        'total_rooms': 55,
        'province': 'Texas'
    },
    {
        'name': 'School 14',
        'email': 'school14@example.com',
        'total_rooms': 65,
        'province': 'Florida'
    },
    {
        'name': 'School 15',
        'email': 'school15@example.com',
        'total_rooms': 75,
        'province': 'Illinois'
    },
    {
        'name': 'School 16',
        'email': 'school16@example.com',
        'total_rooms': 85,
        'province': 'Pennsylvania'
    },
    {
        'name': 'School 17',
        'email': 'school17@example.com',
        'total_rooms': 95,
        'province': 'Ohio'
    },
    {
        'name': 'School 18',
        'email': 'school18@example.com',
        'total_rooms': 100,
        'province': 'Georgia'
    },
    {
        'name': 'School 19',
        'email': 'school19@example.com',
        'total_rooms': 40,
        'province': 'North Carolina'
    },
    {
        'name': 'School 20',
        'email': 'school20@example.com',
        'total_rooms': 50,
        'province': 'Michigan'
    }
]


@school_bp.get('/schools')
def  get_schools():
    page = request.args.get(key='page',default=0,type=int)
    session = Session()
    random_province  = ProvinceService.get_random_province()
    # for _ in range(15):
    #     school = School(
    #         id=str(uuid.uuid4()),  # Generate UUID for the primary key
    #         name=f'Dummy School {_}',
    #         email=f'dummy{_}@example.com',
    #         province='Dummy Province'
    #     )
    # session.add(school)

    # # Commit the changes to the database
    # session.commit()
    result = session.query(School).all()
    
    print(f"result -- {result[0].name}")
    
    return jsonify({
        "message": "result fetched is ",
        "page": page,
        "result": dummy_schools[: page if  page != 0 else len(dummy_schools)],
        "province": random_province
    })
    
@school_bp.get('/schools/<int:id>')
def get_school(id):
    return jsonify({
        "message":"result fetched ",
        "result": dummy_schools[id]
    })

@school_bp.post('/schools/create')
def create_school():
    data = request.data
    db = request.form
    dj = request.json

    print(f'request-json- {dj}\n')
    
    print(f'request-form- {db}\n')

    print(f" data is {data}")

    return jsonify({
        "data": dj
    })

@school_bp.put('/schools/update/<id>')
def update_school(id):
    pass

@school_bp.delete('/schools/delete/<id>')
def delete_school(id):
    pass
