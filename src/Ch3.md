# The Wiki

The hard (cited) and soft (inferred) data found in the previous chapter had been collected into a centralized repository. The repository holds elementary information about the devices stored in a mostly grammar-agnostic corpus akin to Wikipedia's WikiData project [citation needed].
All the changes done on the wiki are tracked by a Git repository, which ensures that data tracks authorship of given info and also relatively (under presumption that data is occasionally checked for up-to-dateness) keeps track of changes on the software side of hardware wallets. 

## Categorized metadata (.c.yaml) files

Device information is split into multiple categories and fields, which is then written into a specialized .c.yaml file. File follows the language of YAML (YAML Ain't Markup Language), which is format for structuralized formatting and serialization of data. The format is inter-changeable with JSON, but compared to JSON, which emphasises formality and completion of data by strict language of closures of data, YAML opts for human-readilibity by not requiring strong verbosity of data closures and using linebreaks for signifying new data/structures.
Due to the variance of categories and relevant inputs, the data in categories is strongly-typed. Which is watched out by a Python 3.7-based compiler [citation needed], and has features: 
- seeks for the files in targetted directories,
- checks for integrity of data, 
    - if any data fails to pass integrity checks, raises appropriate warnings for the user to fix
    - these warnings prevents user from compiling the data, for testing purposes there is a `-f` options, which tries to ignore some of the errors
- looks for symbols and function calls in other files (.md, .html)
- generates various graphs and views on the data based on function calls or by default
The compiler doesn't require a database and stores and uses all data as flat files for easier handling in remote repository environments like Git, SVN or Mercurial. The compiler only handles transformation of data from .c.yaml and other formats into ready-made .md and image/blob files.
The categories used in .c.yaml files need to be formally defined in the compiler itself via specialized .yaml files located in `Compilator/categories`, the files define category key, title, description, data type and optionally a hint. The category key must be globally unique across the entire namespace of all other category keys. The category key is used to key in data in .c.yaml files and also to retrieve them in relevant function calls.
According to known categories and assigned data, the compiler outputs various graphs and plots, which are generated from scripts written in `Compilator/graphs` folder.
The .c.yaml files contain primarily hard data and with some exceptions soft data as well. The remaining soft data is stored in .md Markdown files which contain relevant analyses and remarks found throughout the research of the devices.

## Data model

The data is appropriate modeled using various classes. The elementary classes are Category, CategoryManifest, CategoryValue and DataItem.

// graph showing ERD diagram how individual classes co-dependend on each other

* Category - describes the elementary information about the category, also holds information about the typing and has an embedded value validator, Category may be mandatory or optional
* CategoryManifest - compound class which aggregates multiple Category classes into a manifest, manifest is used to apply various categories of data at once
* CategoryValue - represents a value of said Category which is held by a certain DataItem. Existence of any CategoryValue increments Category counter
* DataItem - is an individual lump of data, which is described by multiple CategoryManifest, CategoryManifest dictates which categories can be held in said DataItem, during deserialization of data the object constructor validates type-corectness and if mandatory fields are satisfied, if either of the conditions fail, the object fails to construct

All categories rely on deserialization of data located either in `Compilator/categories` as .yaml files, this relates to Category and CategoryManifest. In case of CategoryValue and DataItem for data located in `src/` directory with .c.yaml extension. The data model allows for easy extensibility of the compiler.

## Markdown data

Markdown files have an extended syntax by the following:
- Zettelkasten notation - allows linking of other Markdown files for easier navigation and linking [citation needed]
- Custom #~func notation - custom specialized symbol recognized by the compiler which calls custom functions and transforms their outputs into correct markdown or image data.

## Compilation process + website

The data is served under a specialized website which uses an external tool called emanote, a Haskell-based markdown compiler, that transforms .md files into fully-fledged websites akin to Wikipedia. Aside from conversion of websites, it properly handles linking of Zettelkasten links, automatically generates various views for tags, folders and has options for inclusion of external javascript/html/css code either in global context (of the entire website) or in the local context (of a single markdown "page"). [validate]

# Git repository and actions

Handful of bash scripts are written to assist with execution of various steps of the compilation of the repository into a full website. The repository is uploaded into a Git repo which supports execution of post-commit server-side actions, which allow the Git server to handle the newly pushed data and upload changes to the website.
The server-side action does following steps:
1. Runs the compiler
2. If an error is raised during the compilation (i.e. for incorrect typing of data or missing required types), halt, otherwise jump to 3.
3. Merge compiled data with the rest of the repository
4. Pass merged data to Emanote, which operates under Docker/Podman environment and compiles it into a full website.
5. Upload HTML data onto a remote server, credentials are stored under a secret which only the owner has access to.
Similar action runs for all push requests which are submitted to the repository by third-parties. In this case it only runs first 2 steps, and if successful marks push request as good for submission.
