# MODS Table of Contents to Presentation Manifest

This is simply a proof of concept for thinking about leveraging flat table of contents in descriptive metadata in order
to automate the creation of structures in a presentation manifest.

## The Example

Generate.py looks at a manifest.json file and an assumed related descriptive metadata file that we presume describes the
digital object. The sample MODS record has table of contents data that looks like this:

```xml

<tableOfContents>Wheat spindle mosaic virus | 2; Use of fresh and frozen fish | 5; Dietary sulfur on metabolism | 8; Beneficial ground beetles in fields | 11</tableOfContents>

```

Then we split this data into a list of tuples with the label of the section and it's corresponding page number.

We then use the corresponding page number for each page number to match it to a canvas in the manifest file.

Finally, we use this data to build a IIIF structure and replace the `structures` key in the originating manifest with
this.
 