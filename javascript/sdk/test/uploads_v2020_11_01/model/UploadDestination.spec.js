/**
 * Selling Partner API for Uploads
 * The Uploads API lets you upload files that you can programmatically access using other Selling Partner APIs, such as the A+ Content API and the Messaging API.
 *
 * The version of the OpenAPI document: 2020-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import expect from 'expect.js';
import { join } from 'path';

const modulePath = join(process.cwd(), 'src', 'uploads_v2020_11_01', 'index.js');
const SellingPartnerApiForUploads = await import(modulePath);

let instance;

beforeEach(() => {
  try {
    instance = new SellingPartnerApiForUploads.UploadDestination();
  } catch (e) {
    //Handle the cases when this model extends another model by using Model.call(this);
    instance = Object.create(SellingPartnerApiForUploads.UploadDestination.prototype);
  }
});

afterEach(() => {
  instance = null;
});

describe('UploadDestination', () => {
  it('should create an instance of UploadDestination', () => {
    expect(instance).to.be.a(SellingPartnerApiForUploads.UploadDestination);
  });

  it('should have the property uploadDestinationId', () => {
    // verify property exists
    expect(instance).to.have.property('uploadDestinationId');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.uploadDestinationId = expectedValue;
    expect(instance.uploadDestinationId).to.equal(expectedValue);
  });

  it('should have the property url', () => {
    // verify property exists
    expect(instance).to.have.property('url');

    // set and verify value
    const expectedValue = generateMockData('String');
    instance.url = expectedValue;
    expect(instance.url).to.equal(expectedValue);
  });

  it('should have the property headers', () => {
    // verify property exists
    expect(instance).to.have.property('headers');

    // set and verify value
    const expectedValue = generateMockData('Object');
    instance.headers = expectedValue;
    expect(instance.headers).to.equal(expectedValue);
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
        const ModelClass = SellingPartnerApiForUploads[dataType];
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
