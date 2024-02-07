from core import loads_modules, RunAllWebScans
TEST_DOMAIN = 'https://localhost/'


if __name__ == "__main__":
    loads_modules()
    RunAllWebScans(TEST_DOMAIN)

    
    