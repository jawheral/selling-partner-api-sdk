/**
 * Selling Partner API for Shipment Invoicing
 * The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s Fulfillment by Amazon (FBA) orders.
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

const modulePath = join(process.cwd(), 'src', 'invoicing_v0', 'index.js');
const SellingPartnerApiForShipmentInvoicing = await import(modulePath);

let instance;

beforeEach(() => {
  try {
    instance = new SellingPartnerApiForShipmentInvoicing.GetInvoiceStatusResponse();
  } catch (e) {
    //Handle the cases when this model extends another model by using Model.call(this);
    instance = Object.create(SellingPartnerApiForShipmentInvoicing.GetInvoiceStatusResponse.prototype);
  }
});

afterEach(() => {
  instance = null;
});

describe('GetInvoiceStatusResponse', () => {
  it('should create an instance of GetInvoiceStatusResponse', () => {
    expect(instance).to.be.a(SellingPartnerApiForShipmentInvoicing.GetInvoiceStatusResponse);
  });

  it('should have the property payload', () => {
    // verify property exists
    expect(instance).to.have.property('payload');

    // set and verify value
    const expectedValue = generateMockData('ShipmentInvoiceStatusResponse');
    instance.payload = expectedValue;
    expect(instance.payload).to.equal(expectedValue);
  });

  it('should have the property errors', () => {
    // verify property exists
    expect(instance).to.have.property('errors');

    // set and verify value
    const expectedValue = generateMockData('Error', true);
    instance.errors = expectedValue;
    expect(instance.errors).to.equal(expectedValue);
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
        const ModelClass = SellingPartnerApiForShipmentInvoicing[dataType];
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
