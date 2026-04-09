from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm


@login_required
def bandeja_entrada(request):
    recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja_entrada.html', {'recibidos': recibidos})


@login_required
def enviados(request):
    enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/enviados.html', {'enviados': enviados})


@login_required
def ver_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if mensaje.destinatario != request.user and mensaje.remitente != request.user:
        messages.error(request, 'No tenés permiso para ver ese mensaje.')
        return redirect('bandeja-entrada')
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajes/ver_mensaje.html', {'mensaje': mensaje})


@login_required
def enviar_mensaje(request, destinatario_id=None):
    initial = {}
    if destinatario_id:
        destinatario = get_object_or_404(User, pk=destinatario_id)
        initial['destinatario'] = destinatario

    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.remitente = request.user
            nuevo.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja-entrada')
        else:
            messages.error(request, 'Por favor corregí los errores del formulario.')
    else:
        form = MensajeForm(user=request.user, initial=initial)

    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})