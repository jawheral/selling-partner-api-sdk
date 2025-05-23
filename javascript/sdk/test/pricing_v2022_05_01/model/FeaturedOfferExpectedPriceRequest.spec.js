/**
 * Selling Partner API for Pricing
 * The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer pricing information for Amazon Marketplace products.  For more information, refer to the [Product Pricing v2022-05-01 Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide).
 *
 * The version of the OpenAPI document: 2022-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import expect from 'expect.js';
import { join } from 'path';

const modulePath = join(process.cwd(), 'src', 'pricing_v2022_05_01', 'index.js');
const SellingPartnerApiForPricing = await import(modulePath);

let instance;

beforeEach(() => {
  try {
    instance = new SellingPartnerApiForPricing.FeaturedOfferExpectedPriceRequest();
  } catch (e) {
    //Handle the cases when this model extends another model by using Model.call(this);
    instance = Object.create(SellingPartnerApiForPricing.FeaturedOfferExpectedPriceRequest.prototype);
  }
});

afterEach(() => {
  instance = null;
});

describe('FeaturedOfferExpectedPriceRequest', () => {
  it('should create an instance of FeaturedOfferExpectedPriceRequest', () => {
    expect(instance).to.be.a(SellingPartnerApiForPricing.FeaturedOfferExpectedPriceRequest);
  });

  it('should have the property uri', () => {
    // verify property exists
    expect(instance).to.have.property('uri');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.uri = expectedValue;
    expect(instance.uri).to.equal(expectedValue);
  });

  it('should have the property method', () => {
    // verify property exists
    expect(instance).to.have.property('method');

    // set and verify value
    const expectedValue = generateMockData('HttpMethod');
    instance.method = expectedValue;
    expect(instance.method).to.equal(expectedValue);
  });

  it('should have the property body', () => {
    // verify property exists
    expect(instance).to.have.property('body');

    // set and verify value
    const expectedValue = generateMockData('{String: Object}');
    instance.body = expectedValue;
    expect(instance.body).to.equal(expectedValue);
  });

  it('should have the property headers', () => {
    // verify property exists
    expect(instance).to.have.property('headers');

    // set and verify value
    const expectedValue = generateMockData('{String: String}');
    instance.headers = expectedValue;
    expect(instance.headers).to.equal(expectedValue);
  });

  it('should have the property marketplaceId', () => {
    // verify property exists
    expect(instance).to.have.property('marketplaceId');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.marketplaceId = expectedValue;
    expect(instance.marketplaceId).to.equal(expectedValue);
  });

  it('should have the property sku', () => {
    // verify property exists
    expect(instance).to.have.property('sku');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.sku = expectedValue;
    expect(instance.sku).to.equal(expectedValue);
  });

  it('should have the property segment', () => {
    // verify property exists
    expect(instance).to.have.property('segment');

    // set and verify value
    const expectedValue = generateMockData('Segment');
    instance.segment = expectedValue;
    expect(instance.segment).to.equal(expectedValue);
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
        const ModelClass = SellingPartnerApiForPricing[dataType];
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
