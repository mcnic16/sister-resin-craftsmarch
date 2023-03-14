{% extends "base.html" %}
{% load static %}

{% block extra_css %}
    <link rel="stylesheet" href="{% static 'products/css/review.css' %}">
{% endblock %}

{% block page_header %}
<div class="container ">
    <div class="row">
        <div class="col"></div>
    </div>
</div>
{% endblock %}

{% block content %}

<div class="container-fluid header-container">
    <div class="row">
        <div class="col-12 col-md-6 col-lg-4 offset-lg-2">
            <div class="image-container my-5">
                {% if product.image %}
                <a href="{{ product.image.url }}" target="_blank">
                    <img class="card-img-top img-fluid" src="{{ product.image.url }}" alt="{{ product.name }}">
                </a>
                {% else %}
                <a href="">
                    <img class="card-img-top img-fluid" src="{{ MEDIA_URL }}noimage.png" alt="{{ product.name }}">
                </a>
                {% endif %}
            </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4">
            <div class="product-details-container mb-5 mt-md-5">
                <p class="mb-0">{{ product.name }}</p>
                <p class="lead mb-0 text-left font-weight-bold">£{{ product.price }}</p>
                {% if product.category %}
                <p class="small mt-1 mb-0">
                    <a class="text-muted" href="{% url 'products' %}?category={{ product.category.name }}">
                        <i class="fas fa-tag mr-1"></i>{{ product.category.friendly_name }}
                    </a>
                </p>
                {% endif %}
                <p class="mt-3">{{ product.description }}</p>
                <form class="form" action="{% url 'add_to_bag' product.id %}" method="POST">
                    {% csrf_token %}
                    <div class="form-row">
                        <div class="col-12">
                            <p class="mt-3"><strong>Quantity:</strong></p>
                            <div class="form-group w-50">
                                <div class="input-group">
                                <div class="input-group-prepend">
                                    <button class="decrement-qty btn btn-sm btn-black rounded-0"
                                        data-item_id="{{ product.id }}" id="decrement-qty_{{ product.id }}">
                                        <span class="icon ">
                                            <i class="fas fa-minus"></i>
                                        </span>
                                    </button>
                                </div>
                                <input class="form-control qty_input" type="number" name="quantity" value="1" min="1"
                                    max="99" data-item_id="{{ product.id }}" id="id_qty_{{ product.id }}">
                                <div class="input-group-append">
                                    <button class="increment-qty btn btn-sm btn-black rounded-0"
                                        data-item_id="{{ product.id }}" id="increment-qty_{{ product.id }}">
                                        <span class="icon">
                                            <i class="fas fa-plus"></i>
                                    </button>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-12 {% if s %}-12 mt-2{% endif %}">
                        <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 mt-5">
                            <span class="icon">
                                <i class="fas fa-chevron-left"></i>
                            </span>
                            <span class="text-uppercase">Keep Shopping</span>
                        </a>
                        <input type="submit" class="btn btn-black rounded-0 text-uppercase mt-5" value="Add to Bag">
                    </div>
                    <input type="hidden" name="redirect_url" value="{{ request.path }}">
                   
            </div>
            </form>
        </div>
    </div>
</div>
</div>