# Setup

## 1. Launch it

Upload and launch the plugin as any other. It asks for the `data` role and
storage for its raw responses, and no key.

## 2. License its datasets

On the dashboard's **Data sources** page, each of the plugin's three datasets
-- `<instance>:daily`, `<instance>:live` and `<instance>:trades` -- is listed
with Coinbase's Market Data Terms described in words: use and display
inside your organisation; redistribution, display outside it and
applications for other end users need Coinbase's written consent. The
plugin declares no licence. Set each licence there, with a note saying why
(two days kept suits `live` and `trades`); until one is set, the lake keeps
the rows and reads every use right restrictively. What you enter
is what your deployment records; it is not a statement that your use meets
Coinbase's terms (see [Terms](terms.md)).

## 3. Entitle the plugins that read it

On the same page, entitle each reading plugin (a reporting or portfolio
plugin, say) to the datasets it should read. Nothing reads a dataset it is not
entitled to.

## 4. Set the order of sources

Where another plugin also records closes, set which dataset a reader gets
first on the **Data sources** page's priority.

## Agents

An agent you delegate to can read the plugin's two pages through its tools
(`read_connection`, `read_datasets`); the Data sources page has tools of its
own for licences, entitlements and priority.

## Sample data

On a development deployment, the plugin's **Sample data** setting makes it
answer from built-in synthetic responses instead of calling Coinbase, to try
it without reaching Coinbase.
