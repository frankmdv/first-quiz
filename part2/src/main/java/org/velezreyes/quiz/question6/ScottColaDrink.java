package org.velezreyes.quiz.question6;

public class ScottColaDrink implements Drink {
  private String name;
  private double price;
  private boolean isFizzy;

  public ScottColaDrink() {
    this.name = "ScottCola";
    this.price = 0.75;
    this.isFizzy = true;
  }

  @Override
  public String getName() {
    return this.name;
  }

  @Override
  public double getPrice() {
    return this.price;
  }

  @Override
  public boolean isFizzy() {
    return this.isFizzy;
  }
}
