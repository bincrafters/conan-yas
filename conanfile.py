from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "yas"
    version = "7.0.2"
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
        sha256 = "1a4ec905775b815fc862d69fc03c6f23eec50db67976a4c52c8b8ee4b44f52b1"
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
