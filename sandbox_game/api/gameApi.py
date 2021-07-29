from sandbox_game.models import Player
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


@api_view(['POST'])
def submit(request):
    token = request.POST['token']
    gameID = request.POST['gameID']
    teamName = request.POST['teamName']
    userToken = Token.objects.filter(key=token)[0]
    player = Player(playerName=userToken.user.username, teamName=teamName, gameID=gameID)
    player.save()
    data = {
        'username': userToken.user.username,
        'userid': userToken.user_id,
        'gameID': gameID,
        'teamName': teamName,
    }
    return Response(data)
