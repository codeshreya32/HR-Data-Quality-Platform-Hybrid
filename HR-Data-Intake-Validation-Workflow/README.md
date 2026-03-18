# HR Data Quality Platform (V2/Hybrid Version)

This repo is a continuation of the prototype HR workflow project.

### STATUS: ACTIVE DEVELOPMENT
In progress: active setup and restructuring.

## How it's different

### Current Architectural Direction
    -   Excel   --> product surface
    -   Python  --> structural support
    -   SQL     --> SQL-ready design but no full implementation (yet)
    -   Future project compatibility built into structure (for SQL, web UI, etc -- in V3)

### Immediate Changes
    -   cleanup excel workbook structure
    -   revamp data lifecycle (more reliable & optimized) -- using internal record keys for mapping
    -   separate correction/log/issue
    -   solidify folder structure and documentation

## Repo Structure

Will evolve during iterations as version is finalized.

    -   'workbook/' --  Excel workbook & related
    -   'src/'      --  Python modularized support logic
    -   'data/'     --  output & sample dataset
    -   'docs/'     --  documentation*

*architecture, workflow, maps, overall design (like screenshots in v1)


### Next Step Aspirations
    -   Producticized blueprint
    -   Workbook aptly systems mapped
    -   Redesign sheets & respective roles in workbook
    -   rows into entities - document lifecycle change


