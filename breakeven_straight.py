import marimo

__generated_with = "0.9.9"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def __(mo):
    mo.md(
        r"""
        # 1. Importance of Breakeven Hit Rate

        The percentage of bets you need to hit to break even is a critical concept for successful sports betting. It is the point in which your [Expected Value(EV)](https://sportshandle.com/expected-value/) is Zero, meaning in the long run you are expected to not lose, and not make money.

        Understanding the breakeven hit rate is crucial to know if your betting strategy could be profitable and whether you have a Positive EV on any given bet.

        ### A Quick Example: 54% vs 57%
        The breakeven hit rate for the most popular odd availiable, -110 (1.91), is 52.38%. 

        Let's Use these two bettors as an example, each bettor has made a model that consistently finds them good value. Bettor A hits at a 54% rate, bettor B at a 57% rate.
        Although both of these bettors have developed successful models, the compounding of this slight difference in percentage proves to be massively valuable in the long run
        """
    )
    return


@app.cell
def __(np, plt):
    initial_bankroll = 1000 
    odds = -110 
    bet_size_percentage = 0.03 
    number_of_bets = 1000 
    win_probabilities = [0.54, 0.57] 
    num_simulations = 100 


    payout_ratio = 100 / 110

    average_bankrolls = np.zeros((2, number_of_bets + 1))
    average_bankrolls[:, 0] = initial_bankroll

    for bettor in range(2):
        total_bankrolls = np.zeros((num_simulations, number_of_bets + 1))
        total_bankrolls[:, 0] = initial_bankroll

        for sim in range(num_simulations):
            current_bankroll = initial_bankroll
            for bet in range(1, number_of_bets + 1):
                bet_size = current_bankroll * bet_size_percentage
                if np.random.rand() < win_probabilities[bettor]: 
                    current_bankroll += bet_size * payout_ratio
                else:
                    current_bankroll -= bet_size
                total_bankrolls[sim, bet] = current_bankroll

        average_bankrolls[bettor] = np.mean(total_bankrolls, axis=0)

    fig, ax = plt.subplots(figsize=(10, 6))
    labels = ['Bettor 1 (54% hit rate)', 'Bettor 2 (57% hit rate)']
    colors = ['blue', 'orange']

    for i in range(2):
        ax.plot(average_bankrolls[i], label=labels[i], color=colors[i])

    ax.axhline(initial_bankroll, color='black', linestyle='--', label="Starting Bankroll")
    ax.set_title('Monte Carlo Averaged Bankroll Evolution for Two Bettors Over 1000 Bets')
    ax.set_xlabel('Number of Bets')
    ax.set_ylabel('Bankroll ($)')
    ax.legend(loc='upper left')
    ax.grid(True)

    ax # Display on output Marimo
    return (
        average_bankrolls,
        ax,
        bet,
        bet_size,
        bet_size_percentage,
        bettor,
        colors,
        current_bankroll,
        fig,
        i,
        initial_bankroll,
        labels,
        num_simulations,
        number_of_bets,
        odds,
        payout_ratio,
        sim,
        total_bankrolls,
        win_probabilities,
    )


@app.cell
def __(mo):
    mo.md(
        r"""
        <sub> This code simulates two bettors, one with a fifty-four percent hit rate (Blue) and the other with a fifty-seven percent hit rate (Yellow), over one thousand bets. It runs one hundred Monte Carlo simulations, randomly generating bet outcomes based on their win probabilities. Each bettor wagers three percent of their current bankroll, and the average bankroll trajectory across all simulations is calculated and plotted. The graph shows the average bankroll growth for both bettors.

        <sup> The goal of this chart is to show how far a small percentage difference can go when compounded over a significant number of bets
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"""# Calculating Break Even Hit Rate""")
    return


if __name__ == "__main__":
    app.run()
