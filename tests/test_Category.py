def test_category_init(category1, category2):
    assert category1.name == "Автомобили"
    assert category1.description == "Автомобили, как средство передвижения"
    assert len(category1.products) == 3

    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4
