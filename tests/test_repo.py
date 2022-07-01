"""
Foo
"""
import os
import os.path
import shutil
from terradoc.repo.file import create_provider_folder, clone_repo
class TestClass():
    """
    Foo
    """
    # def setup_class(self):
    #     """Foo"""
    #     print("setup_class called once for the class")

    # def setup_method(self):
    #     """Foo"""
    #     print("  setup_method called for every method")

    # def teardown_method(self):
    #     """Foo"""
    #     print("  teardown_method called for every method")

    def teardown_class(self):
        """Foo"""
        # Delete the temp folder we create for the test
        custom_path = "~/tmpDir"
        is_exist = os.path.exists(os.path.expanduser(custom_path))
        if is_exist:
            shutil.rmtree(os.path.expanduser(custom_path))

    def test_create_provider_folder(self):
        """Foo"""
        custom_path = "~/tmpDir"
        create_provider_folder(custom_path)
        assert os.path.exists(os.path.expanduser(custom_path)) is True

    def test_clone_repo(self):
        """Foo"""
        custom_path = "~/tmpDir/terradoc"
        file_to_check = "Readme.md"
        clone_repo("https://github.com/ktasper/terradoc.git",os.path.expanduser(custom_path))
        assert os.path.exists(os.path.expanduser(f"{custom_path}/{file_to_check}"))
