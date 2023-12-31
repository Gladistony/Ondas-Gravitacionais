.. _workflowsegmentsmod:

#######################################
The workflow segment generation module
#######################################

=============
Introduction
=============

This page is designed to give you an introduction to the capabilities of the
pycbc workflow segment generation module and how to use this as part of a pycbc
workflow.

This module is designed to be able to support multiple ways of obtaining these
segments (different codes/interfaces whatever), although new code will always
be needed to support some code/interface that is not currently supported.

This module will generate science segments and any appropriate veto segments
and combine these together to identify a set of segments to be used in the
analysis. The various files will also be returned for later use in the analysis
(ie. for vetoing triggers with data-quality vetoes). If other workflows require 
similar combined files these can be added on request.

=======
Usage
=======

Using this module requires a number of things

* A configuration file (or files) containing the information needed to tell this module how to generate the segments (described below).
* An initialized instance of the pycbc Workflow class, containing the ConfigParser.

The module is then called according to

.. autofunction:: pycbc.workflow.get_segments_file
          :noindex:

-------------------------
Configuration file setup
-------------------------

Here we document the necessary parts of a configuration file for this module.
We'll lay this out in a few blocks. First we'll give an overview of what this might look like in an O3 analysis, to give some background, then we'll give a more comprehensive description of the input format in the `ini` file, and finally we'll explain the full syntax that can be used for individual flags.

^^^^^^^^^^^^^^^^^^^^^^^^^
Example config file
^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: resources/example_dq.ini


Note that this includes both datafind and segment instructions. We'll just
describe the segment options

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description of the ini file contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are three important segments options that we need to provide:

* `segments-science`: This decides what times will be analysed to produce triggers. All times in this might be used to compute PSDs used in the results. Normally all times flagged as ready for science analysis, minus times vetoed at CAT_1.
* `segments-vetoes`: This decides what times will be vetoed when producing final candidate event lists. These times *are* analysed but are discarded after combining single-detector triggers together. Normally the time discarded comprises times vetoed at CAT_2 and times of hardware injections.
* `segments-veto-definer-url`: As previously, this is the location of the veto definer.

Note that this obeys the usual workflow tagging rules. If you supply `segments-science` in `workflow-segments` it will be valid for all ifos. Or, if you want to supply different values for different ifos (e.g. because the Virgo SCIENCE flag is named differently to L1 and H1) you can use `workflow-segments-${ifoname}` (where `${ifoname}` is replaced with the ifo name and this should then be given for all active ifos).

The `segments-science` and `segments-vetoes` are provided as a *comma-separated* list of flags. Documented below.

^^^^^^^^^^^^^^^^^^^^^
Flag syntax
^^^^^^^^^^^^^^^^^^^^^

We've said that `segments-science` and `segments-vetoes` look something like

`segments-science = FLAG_1,FLAG_2`

We start with a simple example of what can be given as the value of FLAG_1:

`+SCIENCE` or `-SCIENCE`

In this case SCIENCE is the flag name. It is what will be queried from the segment server. The ifo will be automatically appended, so this becomes `${IFO}:SCIENCE` when querying. The `+` or `-` is important and not optional. If the sign as a `+` then the flag is added to the list of times, if it is `-` then the flag is removed. All `+` flags are processed first and then all `-` flags are removed from that.

In `segments-science` `+` means that that time should be included in the analysis. A `-` means it should not be included.

In `segments-vetoes` `+` means that that time should be included in the vetoed times and so not included in the analysis. A `-` means it should not be included in the vetoed times so that time will be analysed ... It is not envisaged that `-` flags will be used often in `segments-vetoes`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
Version numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For LVC internal usage, flags should be provided with a version number. So this would be:

`+SCIENCE:1` or `-SCIENCE:1`

not providing a version will query *all* versions of that flag. That probably won't be a good thing with a flag like `SCIENCE`, but will be okay if there is only one version of the flag. In general, for LVC usage provide a version number! For GWOSC usage there are no version numbers.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
The veto-definer file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The veto definer file groups a set of flags together, defining what is meant as CAT_1 vetoes. We could explicitly map the veto-definer from the XML file into a list of flags (removing the veto-definer altogether), but it is easier to just use the veto-definer and let the detchar group decide what these flags should be. 

When using a veto-definer we have access to "special" flag names corresponding to what's in the veto-definer. These special flag names are:

* `CAT_1`: All flags given the `category` value of 1 within the veto-definer file.
* `CAT_2`: All flags given the `category` value of 2 within the veto-definer file.
* `CAT_H`: All flags given the `category` value of 3 within the veto-definer file. There's some history/confusion here: since S6 we've been storing hardware injections in the `category=3` field of the veto-definer. Don't worry about that, this just means all hardware injection flags.
* `CAT_3`. All flags given the `category` value of 4 within the veto-definer file. As mentioned above, this is where category 3 vetoes are traditionally stored. These vetoes have not been used since the start of Advanced LIGO/Virgo, so we can probably ignore this now.

Examples of using these flags are given at the top. All of the stuff below also applies to these "special" flags, but some of these combinations may be a little odd.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Adding a ifo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's start adding complexity. I can explicitly state an ifo, even if the workflow thinks it's analysing V1, I can supply a *different* ifo and the workflow will analyse that data as if it was the second ifo. For example

`segments-science-v1 = H1:DMT-ANALYSIS_READY:1`

will use `H1` data as "Virgo". This functionality is not expected to be used in production runs, but has been useful in the past for testing purposes, e.g. using H1 data as V1 to simulate a true 3-instrument analysis. Probably this won't be used much, but it's here for completeness.

~~~~~~~~~~~~~~~~~~~~~~
Providing padding
~~~~~~~~~~~~~~~~~~~~~~

For some flags we want to include some additional time ... Normally for vetoes where we want to cut out a little bit more data as we know the bad time might be a little longer than that recorded. This can be done as:

`+H1:SCIENCE:1<-8:8>` or `-H1:SCIENCE:1<-8:8>`

This corresponds to `start_pad` = -8 and `end_pad` = 8. These numbers are added to the start/end times of every segment coming from this flag, so `segment_start += start_pad` and `segment_end += end_pad`.  Or more simply, in this example the segment is extended by 8s on both the start and the end of every segment.
This number can be flipped to cause the segment to get shorter. Be careful with this though, glue does not do the right thing if the start of a segment is after the end of the segment - e.g. if you shrink a segment so much that it disappears, weird things will happen!

The padding must always appear after the flag and version name.

~~~~~~~~~~~~~~~~~~~~~~~~
Providing valid times
~~~~~~~~~~~~~~~~~~~~~~~~

Some flags are valid between a specific range of times. So if we provide:

`+H1:SCIENCE:1[0:1000000000]` or `-H1:SCIENCE:1[0:1000000000]`

it means that we only query the `SCIENCE` flag for times in [0:1000000000]. If this flag is active outside of this time range, we do not use it.

At the moment it is not possible to provide a flag that is active in two distinct ranges, but not in between. If that functionality is required, it can probably be added.

Valid times must also be provided after the flag name and version. If providing *both* this and a padding it would look like:

`+H1:SCIENCE:1<-8:8>[0:1000000000]` or `-H1:SCIENCE:1<-8:8>[0:1000000000]`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtaining segments from pre-existing XML files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of obtaining science and veto segments from a segment database and veto
definer file, they can be read directly from XML segment files. This can be
useful, for example, to test new kinds of vetoes. To do this, use the following
options in the `[workflow-segments]` section:

* `segments-source = file`
* `segments-science-file = /path/to/science/segments/file.xml`
* `segments-vetoes-file = /path/to/veto/segments/file.xml`

In order for this to work, the `name` field of the `segment_definer` tables of
the science and vetoes files should be set to `science` and `vetoes`
respectively.


==========================================
:mod:`pycbc.workflow.segment` Module
==========================================

This is complete documentation of this module's code

.. automodule:: pycbc.workflow.segment 
    :noindex:
    :members:
    :undoc-members:
    :show-inheritance:

