from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "yas"
    version = "7.0.3"
    description = "Yet Another Serialization"
    topics = ("conan", "yas", "serialization")
    url = "https://github.com/bincrafters/conan-yas"
    homepage = "https://github.com/niXman/yas"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSL-1.0"
    no_copy_source = True
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "dbee4e170d5a27b9ef4757f3daf47a906dd60c5d53b7db2d129519cab5b32cdb"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _extract_license(self):
        header = tools.load(os.path.join(self.source_folder, self._source_subfolder, "include", "yas", "binary_oarchive.hpp"))
        license_contents = header[:header.find("#", 1)].replace("//", "")
        tools.save("LICENSE", license_contents)

    def package(self):
        self._extract_license()
        self.copy(pattern="*", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("LICENSE", dst="licenses")

    def package_id(self):
        self.info.header_only()
