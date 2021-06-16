
import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)


def getMovieInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def putMovieInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    body = json.loads(event["body"])
    print(body)
    print(movie_id)
    item = {
        'pk': movie_id,
        'sk': 'info',
        'tittle': body["tittle"],
        'main_actor_01': body["main_actor_01"],
        'main_actor_02': body["main_actor_02"],
        'main_actor_03': body["main_actor_03"],
        'year': body["year"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getMovieByRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    cinema_room_id = path.split("/")[-1] # ["user", "id"]
    movie_id = path.split("/")[-3] # ["user", "id"]
    body = json.loads(event["body"])
    response = table.get_item(
        Key={
            'pk': cinema_room_id,
            'sk': movie_id
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def getCinemaRoomInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    cinema_room_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': cinema_room_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putCinemaRoomInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    cinema_room_id = path.split("/")[-1] # ["user", "id"]
    body = json.loads(event["body"])
    print(body)
    print(cinema_room_id)
    item = {
        'pk': cinema_room_id,
        'sk': 'info',
        'room': body["room"], 
        '2D': body["2D"],
        '3D': body["3D"],
        'number_Seats':body["number_Seats"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
def getViewerInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    viewer_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': viewer_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putViewerInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    viewer_id = path.split("/")[-1] # ["user", "id"]
    body = json.loads(event["body"])
    print(body)
    print(viewer_id)
    item = {
        'pk': viewer_id,
        'sk': 'info',
        'name': body["name"],
        'age': body["age"]

    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getDateInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    date_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': date_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }