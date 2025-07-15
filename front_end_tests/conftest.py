def pytest_addoption(parser):
    print("✅ conftest.py loaded and hook called")
    parser.addoption(
        "--max-commands", action="store", default=5, type=int,
        help="Maximum number of commands to test"
    )
    parser.addoption(
        "--max-graphs", action="store", default=5, type=int,
        help="Maximum number of graphs to test"
    )
