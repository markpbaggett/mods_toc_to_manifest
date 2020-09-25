import xmltodict
import json
import uuid


class PresentationManifest:
    def __init__(self, path_to_manifest, path_to_metadata):
        self.manifest_path = path_to_manifest
        self.path_to_metadata = path_to_metadata
        self.manifest = self.__read_manifest(path_to_manifest)
        self.canvases = self.__get_canvases()
        self.sections = self.__get_toc(path_to_metadata)
        self.structures = self.__build_structures()
        self.json = self.__inject_structures()

    @staticmethod
    def __read_manifest(manifest):
        with open(manifest, "r") as my_manifest:
            return json.load(my_manifest)

    @staticmethod
    def __get_toc(metadata):
        with open(metadata, "rb") as mods:
            sections = []
            try:
                toc = xmltodict.parse(mods)["mods"]["tableOfContents"].split(";")
                for section in toc:
                    sections.append((section.split(" | ")[0], section.split(" | ")[1]))
                return sections
            except KeyError:
                return sections

    def __get_canvases(self):
        return [canvas["@id"] for canvas in self.manifest["sequences"][0]["canvases"]]

    def __build_structures(self):
        if len(self.sections) > 0:
            toc = {
                "@id": "http://example.org/iiif/book1/range/r0",
                "@type": "sc:Range",
                "label": "Table of Contents",
                "members": [],
            }
            additional_structures = []
            for section in self.sections:
                section_id = f"http://{uuid.uuid4()}"
                toc["members"].append(self.__add_member(section[0], section_id))
                additional_structures.append(
                    self.__additional_structure(
                        section[0], section_id, self.canvases[int(section[1]) - 1]
                    )
                )
            return self.__final_structures(toc, additional_structures)

    @staticmethod
    def __add_member(label, identifier):
        return {"@id": identifier, "@type": "sc:Range", "label": label}

    @staticmethod
    def __additional_structure(label, identifier, canvas):
        return {
            "@id": identifier,
            "@type": "sc:Range",
            "label": label,
            "canvases": [canvas],
        }

    @staticmethod
    def __final_structures(contents, extras):
        final = [contents]
        for extra in extras:
            final.append(extra)
        return final

    def __inject_structures(self):
        new_manifest = self.manifest
        new_manifest["structures"] = self.structures
        return json.dumps(new_manifest)


if __name__ == "__main__":
    x = PresentationManifest(
        "/home/mark/iiif-workshop/presentation_manifests/manifest_toc.json",
        "samples/agrtfhs_3303.xml",
    )
    print(x.json)
