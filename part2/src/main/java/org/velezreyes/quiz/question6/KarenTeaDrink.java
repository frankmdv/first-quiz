package org.velezreyes.quiz.question6;

public class KarenTeaDrink implements Drink {
  private String name;
  private double price;
  private boolean isFizzy;

  public KarenTeaDrink() {
    this.name = "KarenTea";
    this.price = 1;
    this.isFizzy = false;
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
