/**
 * Selling Partner API for Orders
 * Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.   _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).
 *
 * The version of the OpenAPI document: v0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import expect from 'expect.js';
import { join } from 'path';

const modulePath = join(process.cwd(), 'src', 'orders_v0', 'index.js');
const SellingPartnerApiForOrders = await import(modulePath);

let instance;

beforeEach(() => {
  try {
    instance = new SellingPartnerApiForOrders.OrderAddress();
  } catch (e) {
    //Handle the cases when this model extends another model by using Model.call(this);
    instance = Object.create(SellingPartnerApiForOrders.OrderAddress.prototype);
  }
});

afterEach(() => {
  instance = null;
});

describe('OrderAddress', () => {
  it('should create an instance of OrderAddress', () => {
    expect(instance).to.be.a(SellingPartnerApiForOrders.OrderAddress);
  });

  it('should have the property amazonOrderId', () => {
    // verify property exists
    expect(instance).to.have.property('amazonOrderId');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.amazonOrderId = expectedValue;
    expect(instance.amazonOrderId).to.equal(expectedValue);
  });

  it('should have the property buyerCompanyName', () => {
    // verify property exists
    expect(instance).to.have.property('buyerCompanyName');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.buyerCompanyName = expectedValue;
    expect(instance.buyerCompanyName).to.equal(expectedValue);
  });

  it('should have the property shippingAddress', () => {
    // verify property exists
    expect(instance).to.have.property('shippingAddress');

    // set and verify value
    const expectedValue = generateMockData('Address');
    instance.shippingAddress = expectedValue;
    expect(instance.shippingAddress).to.equal(expectedValue);
  });

  it('should have the property deliveryPreferences', () => {
    // verify property exists
    expect(instance).to.have.property('deliveryPreferences');

    // set and verify value
    const expectedValue = generateMockData('DeliveryPreferences');
    instance.deliveryPreferences = expectedValue;
    expect(instance.deliveryPreferences).to.equal(expectedValue);
  });

});

// Helper function to generate random test data
function generateMockData(dataType, isArray = false) {
  if (!dataType) return {};

  // Handle array types
  if (isArray) {
    return [generateMockData(dataType), generateMockData(dataType)];
  }

  switch(dataType) {
    case 'String':
      return 'mock-' + Math.random().toString(36).substring(2, 10);
    case 'Number':
      return Math.floor(Math.random() * 1000);
    case 'Boolean':
      return Math.random() > 0.5;
    case 'Date':
      return new Date().toISOString();
    default:
      try {
        const ModelClass = SellingPartnerApiForOrders[dataType];
        if (ModelClass) {
          const instance = Object.create(ModelClass.prototype);
          return instance;
        }
      } catch (e) {
        console.error("Error creating instance of", dataType);
        return {};
      }
      return {};
  }
}
