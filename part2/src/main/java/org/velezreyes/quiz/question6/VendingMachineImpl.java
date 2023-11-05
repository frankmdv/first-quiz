package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
  private double moneyInserted;

  public VendingMachineImpl() {
    this.moneyInserted = 0;
  }

  @Override
  public void insertQuarter() {
    this.moneyInserted += 0.25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    Drink pressedDrink;
    switch (name) {
      case "ScottCola":
        pressedDrink = new ScottColaDrink();
        break;
      case "KarenTea":
        pressedDrink = new KarenTeaDrink();
        break;
      default:
        throw new UnknownDrinkException();
    }

    this.processDrinkTransaction(pressedDrink.getPrice());
    return pressedDrink;
  }

  private void processDrinkTransaction(double drinkPrice) throws NotEnoughMoneyException {
    if (this.moneyInserted < drinkPrice) throw new NotEnoughMoneyException();
    this.moneyInserted -= drinkPrice;
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }
}
