from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from modules.vps.models import VPS
from modules.vps.serializers import VPSSerializer


class VPSCreateAPIView(APIView):
    def post(self, request):
        serializer = VPSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VPSDetailAPIView(APIView):
    def get(self, request, uid):
        try:
            vps = VPS.objects.get(uid=uid)
        except VPS.DoesNotExist:
            return Response({"error": "VPS not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = VPSSerializer(vps)
        return Response(serializer.data)


class VPSListAPIView(ListAPIView):
    serializer_class = VPSSerializer

    def get_queryset(self):
        queryset = VPS.objects.all()
        cpu = self.request.query_params.get('cpu')
        ram = self.request.query_params.get('ram')
        status = self.request.query_params.get('status')
        if cpu:
            queryset = queryset.filter(cpu=cpu)
        if ram:
            queryset = queryset.filter(ram=ram)
        if status:
            queryset = queryset.filter(status=status.lower())

        return queryset


class VPSStatusUpdateAPIView(APIView):
    def patch(self, request, uid):
        try:
            vps = VPS.objects.get(uid=uid)
        except VPS.DoesNotExist:
            return Response({"error": "VPS not found"}, status=status.HTTP_404_NOT_FOUND)

        status_value = request.data.get('status')
        if status_value not in dict(VPS.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        vps.status = status_value
        vps.save()
        serializer = VPSSerializer(vps)
        return Response(serializer.data)
