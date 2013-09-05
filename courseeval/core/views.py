
def index(request):
    return HttpResponse("asdf!")
    return render(request, 'admin/index.html')

def delete(request):
    errorMsg = ''
    if 'card_id' in request.POST:
        card_id = request.POST['card_id']
        card = Card.objects.get(id=card_id)
        card.delete()
        return HttpResponse('{"success": true}', mimetype="application/json")
    else:
        errorMsg = "card_id not provided."
    return HttpResponse('{"success": true, "error": "%s"}' % errorMsg, mimetype="application/json")
    #return redirect(index)
    #else:
    #return render(request, 'collections/create.html')
    