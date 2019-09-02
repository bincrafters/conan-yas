from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "yas"
    version = "7.0.2"
    description = "Yet Another Serialization"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "yas", "serialization")
    url = "https://github.com/bverhagen/conan-yas"
    homepage = "https://github.com/niXman/yas"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSL-1.0"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/niXman/yas"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256="1a4ec905775b815fc862d69fc03c6f23eec50db67976a4c52c8b8ee4b44f52b1")
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
