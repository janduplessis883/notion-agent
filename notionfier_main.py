import dataclasses
import mistune
import notion_client

import notionfier.plugins.footnotes


def append_markdown_to_notion_page(token: str, page_id: str, markdown_content: str):
    """
    Appends Markdown content as blocks to an existing Notion page.

    Args:
        token (str): The Notion auth token.
        page_id (str): The ID of the Notion page where blocks will be appended.
        markdown_content (str): The Markdown content to be processed.

    """
    # Create a Mistune Markdown renderer with plugins
    md = mistune.create_markdown(
        renderer=notionfier.MyRenderer(),
        plugins=[
            mistune.plugins.plugin_task_lists,
            mistune.plugins.plugin_table,
            mistune.plugins.plugin_url,
            mistune.plugins.plugin_def_list,
            mistune.plugins.plugin_strikethrough,
            notionfier.plugins.plugin_footnotes,
        ],
    )
    # Render Markdown content to Notion blocks
    result = md(markdown_content)

    # Convert blocks to the format expected by the Notion API
    children = [
        dataclasses.asdict(x, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        for x in result
    ]

    # Initialize Notion client
    client = notion_client.Client(auth=token)

    # Append blocks to the specified Notion page
    client.blocks.children.append(block_id=page_id, children=children)


# Example usage
if __name__ == "__main__":
    # Replace these with your own values
    NOTION_TOKEN = "secret_AUqFdk1kzS6qe7iw0LVlPDQXJ1TrDxnM7n9ZIB5fOlB"
    PAGE_ID = "160fdfd68a9781c9aaeaefee3783e642"

    # Markdown content received from an LLM or other source
    markdown_content = """# Comprehensive Report on Equipment Requirements for Clinical Research in UK Primary Care Settings

## Executive Summary

This report outlines the essential equipment and guidelines necessary for conducting clinical research in UK primary care settings, as per NHS England directives. It categorizes the required tools into basic and specialized equipment, emphasizes the importance of compliance with clinical and data protection standards, and provides actionable recommendations for improving the quality and safety of clinical research activities. The report aims to assist healthcare professionals and stakeholders in understanding and implementing the necessary requirements for effective research in their practices.


"""


    append_markdown_to_notion_page(NOTION_TOKEN, PAGE_ID, markdown_content)
