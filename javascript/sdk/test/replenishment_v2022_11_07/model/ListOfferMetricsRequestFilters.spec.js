/**
 * Selling Partner API for Replenishment
 * The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.  The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.
 *
 * The version of the OpenAPI document: 2022-11-07
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import expect from 'expect.js';
import { join } from 'path';

const modulePath = join(process.cwd(), 'src', 'replenishment_v2022_11_07', 'index.js');
const SellingPartnerApiForReplenishment = await import(modulePath);

let instance;

beforeEach(() => {
  try {
    instance = new SellingPartnerApiForReplenishment.ListOfferMetricsRequestFilters();
  } catch (e) {
    //Handle the cases when this model extends another model by using Model.call(this);
    instance = Object.create(SellingPartnerApiForReplenishment.ListOfferMetricsRequestFilters.prototype);
  }
});

afterEach(() => {
  instance = null;
});

describe('ListOfferMetricsRequestFilters', () => {
  it('should create an instance of ListOfferMetricsRequestFilters', () => {
    expect(instance).to.be.a(SellingPartnerApiForReplenishment.ListOfferMetricsRequestFilters);
  });

  it('should have the property aggregationFrequency', () => {
    // verify property exists
    expect(instance).to.have.property('aggregationFrequency');

    // set and verify value
    const expectedValue = generateMockData('AggregationFrequency');
    instance.aggregationFrequency = expectedValue;
    expect(instance.aggregationFrequency).to.equal(expectedValue);
  });

  it('should have the property timeInterval', () => {
    // verify property exists
    expect(instance).to.have.property('timeInterval');

    // set and verify value
    const expectedValue = generateMockData('TimeInterval');
    instance.timeInterval = expectedValue;
    expect(instance.timeInterval).to.equal(expectedValue);
  });

  it('should have the property timePeriodType', () => {
    // verify property exists
    expect(instance).to.have.property('timePeriodType');

    // set and verify value
    const expectedValue = generateMockData('TimePeriodType');
    instance.timePeriodType = expectedValue;
    expect(instance.timePeriodType).to.equal(expectedValue);
  });

  it('should have the property marketplaceId', () => {
    // verify property exists
    expect(instance).to.have.property('marketplaceId');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.marketplaceId = expectedValue;
    expect(instance.marketplaceId).to.equal(expectedValue);
  });

  it('should have the property programTypes', () => {
    // verify property exists
    expect(instance).to.have.property('programTypes');

    // set and verify value
    const expectedValue = generateMockData('ProgramType', true);
    instance.programTypes = expectedValue;
    expect(instance.programTypes).to.equal(expectedValue);
  });

  it('should have the property asins', () => {
    // verify property exists
    expect(instance).to.have.property('asins');

    // set and verify value
    const expectedValue = generateMockData('String', true);
    instance.asins = expectedValue;
    expect(instance.asins).to.equal(expectedValue);
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
        const ModelClass = SellingPartnerApiForReplenishment[dataType];
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
