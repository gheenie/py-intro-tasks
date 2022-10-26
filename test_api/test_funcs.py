def check (got, want):
    try:
        assert got == want
        print('✅ test passing!')
    except:
        print(f'❌ test failing: expected: {want}, got: {got}')