# MODS Table of Contents to Presentation Manifest

This is simply a proof of concept for thinking about leveraging flat table of contents in descriptive metadata in order
to automate the creation of structures in a presentation manifest.

## The Example

Generate.py looks at a manifest.json file and an assumed related descriptive metadata file that we assume describes the
digital object. The sample MODS record has table of contents data that looks like this:

```xml

<tableOfContents>Wheat spindle mosaic virus | 2; Use of fresh and frozen fish | 5; Dietary sulfur on metabolism | 8; Beneficial ground beetles in fields | 11</tableOfContents>

```

Then we split this data into a list of tuples with the label of the section and it's corresponding page number. 

Finally, this data is leveraged to create structures that correspond to each page.
 