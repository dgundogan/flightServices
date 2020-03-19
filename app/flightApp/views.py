from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                    arrivalCity=request.data['arrivalCity'],
                                    dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    
    passenger = Passenger()
    passenger.firtname = request.data['firstName']
    passenger.lastname = request.data['lastname']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    
    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    
    Reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)
    
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassangerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
