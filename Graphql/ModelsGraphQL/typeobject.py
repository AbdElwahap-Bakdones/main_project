from core import models
from graphene_django import DjangoObjectType
from graphene import relay
import graphene


class UserObjectType(DjangoObjectType):
    class Meta:
        model = models.User
        fields = ['pk', 'first_name', 'last_name',
                  'email', 'phone', 'username']
        interfaces = (relay.Node,)


class PlayerObjectType(DjangoObjectType):
    class Meta:
        model = models.Player
        fields = ['location_lat', 'location_long', 'user_id']
        interfaces = (relay.Node,)


class ManagerObjectType(DjangoObjectType):
    class Meta:
        model = models.Manager
        fields = ['id']


class SubManagerObjectType(DjangoObjectType):
    class Meta:
        model = models.SubManager
        fields = ['user_id']
        interfaces = (relay.Node,)


class ClubObjectType(DjangoObjectType):
    manager_id = graphene.Field(ManagerObjectType)
    pk = graphene.Field(type=graphene.Int, source='id')

    class Meta:
        model = models.Club
        fields = ['id', 'pk', 'name', 'location',
                  'number_stad', 'is_available', 'manager_id']
        interfaces = (relay.Node,)


class SectionObjectType(DjangoObjectType):
    pk = graphene.Field(type=graphene.Int, source='id')

    class Meta:
        model = models.Section
        fields = ['id', 'pk', 'name', 'is_available',
                  'club_id', 'sub_manager_id']
        interfaces = (relay.Node,)


class StadiumObjectType(DjangoObjectType):
    class Meta:
        model = models.Stadium
        fields = "__all__"
        interfaces = (relay.Node,)


class ServiceObjectType(DjangoObjectType):
    class Meta:
        model = models.Service
        fields = "__all__"
        interfaces = (relay.Node,)


class StadiumServiceObjectType(DjangoObjectType):
    class Meta:
        model = models.StadiumService
        fields = "__all__"
        interfaces = (relay.Node,)


class DurationObjectType(DjangoObjectType):
    class Meta:
        model = models.Duration
        fields = "__all__"
        interfaces = (relay.Node,)


class ReservationObjectType(DjangoObjectType):
    class Meta:
        model = models.Reservation
        fields = "__all__"
        interfaces = (relay.Node,)


class Player_reservationObjectType(DjangoObjectType):
    class Meta:
        model = models.Player_reservation
        fields = "__all__"
        interfaces = (relay.Node,)


class Player_reservationObjectType(DjangoObjectType):
    class Meta:
        model = models.Player_reservation
        fields = "__all__"
        interfaces = (relay.Node,)


class TeamObjectType(DjangoObjectType):
    pk = graphene.Field(type=graphene.Int, source='id')

    class Meta:
        model = models.Team
        fields = ['id', 'pk', 'name', 'type_id', 'search_game', 'temp']
        interfaces = (relay.Node,)


class Team_resevationObjectType(DjangoObjectType):
    class Meta:
        model = models.Team_resevation
        fields = "__all__"
        interfaces = (relay.Node,)


class Team_membersObjectType(DjangoObjectType):
    class Meta:
        model = models.Team_members
        fields = "__all__"
        interfaces = (relay.Node,)


class PostionObjectType(DjangoObjectType):
    class Meta:
        model = models.Position
        fields = "__all__"
        interfaces = (relay.Node,)


class TypeObjectType(DjangoObjectType):
    class Meta:
        model = models.Type
        fields = "__all__"
        interfaces = (relay.Node,)


class StadiumRateObjectType(DjangoObjectType):
    class Meta:
        model = models.StadiumRate
        fields = "__all__"
        interfaces = (relay.Node,)


class UserRateObjectType(DjangoObjectType):
    class Meta:
        model = models.UserRate
        fields = "__all__"
        interfaces = (relay.Node,)


class RateTypeObjectType(DjangoObjectType):
    class Meta:
        model = models.RateType
        fields = "__all__"
        interfaces = (relay.Node,)


class NotificationObjectType(DjangoObjectType):
    class Meta:
        model = models.Notification
        fields = "__all__"
        interfaces = (relay.Node,)


class FriendObjectType(DjangoObjectType):
    pk = graphene.Field(type=graphene.Int, source='id')
    friends = graphene.Field(type=PlayerObjectType, source='player2')
    me = graphene.Field(type=graphene.ID, source='player1')

    class Meta:
        model = models.Friend
        fields = ['id', 'pk', 'friends', 'me']
        interfaces = (relay.Node,)