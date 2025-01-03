# filepath: /Users/maamounmraish/AIInvestingTool/prompts.py
def stock_recommendation_prompt(tickers, indicator):
    """
    Generates a prompt for stock analysis based on selected tickers and indicator.

    Args:
        tickers (list): A list of selected stock tickers.
        indicator (str): The indicator to analyze (e.g., price, volume, market cap).

    Returns:
        str: A formatted prompt for OpenAI API to generate stock analysis.
    """
    return (
        f"Analyze the following stocks: {', '.join(tickers)} based on the indicator '{indicator}'. "
        "Provide stock recommendations and insights in a concise and professional manner."
    )
