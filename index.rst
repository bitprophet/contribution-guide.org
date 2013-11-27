====================================
Contributing to Open Source Projects
====================================


About
=====

This document provides a set of best practices for open source contributions -
bug reports, code submissions / pull requests, etc.

For the most part, these guidelines apply equally to *any* project regardless
of programming language or topic. Where applicable, we outline where individual
projects may have additional requirements.

Naturally, this document is itself open source, and we encourage feedback &
suggestions for improvement.


.. contents::


Submitting bugs
===============

Due diligence
-------------

Before submitting a bug, please do the following:

* Perform basic troubleshooting steps:

    * **Make sure you're on the latest version.** If you're not on the most recent
      version, your problem may have been solved already! Upgrading is always the
      best first step.
    * **Try older versions.** If you're already *on* the latest release, try
      rolling back a few minor versions (e.g. if on 1.7, try 1.5 or 1.6) and
      see if the problem goes away. This will help the devs narrow down when
      the problem first arose in the commit log.
    * **Try switching up dependency versions.** If the software in question has
      dependencies (other libraries, etc) try upgrading/downgrading those as
      well.

* Search the project's bug/issue tracker to make sure it's not a known issue.
* Check with the mailing list and/or IRC channel in case the problem is
  non-bug-related.

Bug report etiquette
--------------------

If you've found a new bug, the developers will doubtless want to hear about it!
Make sure your report gets the attention it deserves: bug reports with missing
information may get skipped over or punted back to you, delaying work on a fix.
The below constitutes a bare minimum; generally, more info is better:

* **What version of the core programming language interpreter/compiler are you
  using?** For example, if it's a Python project, are you using Python 2.7.3?
  Python 3.3.1? PyPy 2.0?
* **What operating system are you on?** Windows? (Vista? 7? 32-bit? 64-bit?)
  Mac OS X?  (10.7.4? 10.9.0?) Linux? (Which distro? Which version of that
  distro? 32 or
  64 bits?) Again, the more details, the better.
* **Which version or versions of the software are you using?** Ideally, you
  followed the advice above and have ruled out (or verified that the problem
  exists in) a few different versions. Even if you didn't, at least say which
  version you're running now.
* **How can the developers recreate the bug on their end?** If at all possible,
  include a copy of your code, the command you used to invoke it, and the full
  output of your run (if applicable.)
  
    * A common tactic is to quickly chop out chunks of your code until a simple
      (but still bug-causing) "base case" remains. Not only can this help you
      identify problems which aren't real bugs, but it means the developer can
      get to fixing the bug faster.


Contributing bugfixes or features
=================================

.. warning::
    Please follow these instructions closely! Your patch will not be accepted
    (or will at least be delayed) otherwise. Thanks!

Which branch to work out of
---------------------------

We split development into two primary branches:

* **Bug fixes** go into a branch named after the **current stable release
  line** (e.g. 1.0, 1.1, 1.2 etc).

    * Caveat: bug fixes requiring large changes to the code or which have a
      chance of being otherwise disruptive, may need to go in **master**
      instead. This is a judgement call -- ask the devs!

* **New features** go into **the master branch**.

    * Note that depending on how long it takes for the dev team to merge your
      patch, the copy of ``master`` you worked off of may get out of date! If
      you find yourself 'bumping' a pull request that's been sidelined for a
      while, **make sure you rebase or merge to latest master** to ensure a
      speedier resolution.

Code formatting
---------------

We follow `PEP-8 <http://www.python.org/dev/peps/pep-0008/>`_ whenever it makes
sense, which is most of the time. At the very least, please make sure you put
spaces after your commas within list-like syntax (``[this,is,not,ok]`` but
``[this, is, fine]``; ditto for ``function(calls, like, this)``) and keep your
variables ``lower_cased_and_underscored``, with only classes being
``CamelCased``.

Documentation isn't optional
----------------------------

It's not! Patches without documentation will be returned to sender.
Specifically, by "documentation" we mean:

* **Docstrings** must be created or updated for public API
  functions/methods/etc.

    * Don't forget to include `versionadded
      <http://sphinx-doc.org/markup/para.html#directive-versionadded>`_/`versionchanged
      <http://sphinx-doc.org/markup/para.html#directive-versionchanged>`_ ReST
      directives at the bottom of any new or changed docstrings!
    * Use ``versionadded`` for truly new API members -- new methods, functions,
      classes or modules.
    * Use ``versionchanged`` when adding/removing new function/method
      arguments, or whenever behavior changes.

* New features should ideally include updates to **prose documentation**,
  including useful example code snippets.
* All changes (**including bugfixes**) should have a **changelog entry**
  crediting the contributor and/or any individuals instrumental in identifying
  the problem.

Tests aren't optional
---------------------

We aim for very high code coverage. Any bugfix that doesn't include a test
proving the existence of the bug being fixed (and of course, that passes when
the bugfix is applied) may be suspect.

We've found that test-first development really helps make features better
architected and identifies potential edge cases earlier instead of later. New
features should also include thorough tests.
