def test_func(got, want):
    try:
        assert got == want
        print("yay")
    except:
        print(f"function returned {got}, wanted {want}")
