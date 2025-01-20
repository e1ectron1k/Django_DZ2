from django.shortcuts import render

from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_view(request, recipe_name):
    if recipe_name not in DATA:
        raise Http404("Рецепт не найден")

    recipe = DATA[recipe_name]

    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError("Количество порций должно быть положительным")
    except ValueError:
        servings = 1

    adjusted_recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}

    context = {
        'recipe': adjusted_recipe,
    }

    return render(request, 'calculator/index.html', context)