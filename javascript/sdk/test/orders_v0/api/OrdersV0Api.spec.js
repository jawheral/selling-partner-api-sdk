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
import sinon from 'sinon';
import { join } from 'path';

const modulePath = join(process.cwd(), 'src', 'orders_v0', 'index.js');
const SellingPartnerApiForOrders = await import(modulePath);

let instance;
let sandbox;
const testEndpoint = 'https://localhost:3000';
const testAccessToken = "testAccessToken";

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

// Generate mock requests and responses for each operation
const mockconfirmShipmentData = {
  request: {
    'orderId': generateMockData('String'),
    'payload': generateMockData('ConfirmShipmentRequest')
  },
  response: {
    statusCode: 204,
    headers: {}
  }
};
const mockgetOrderData = {
  request: {
    'orderId': generateMockData('String')
  },
  response: {
    data: generateMockData('GetOrderResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrderAddressData = {
  request: {
    'orderId': generateMockData('String')
  },
  response: {
    data: generateMockData('GetOrderAddressResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrderBuyerInfoData = {
  request: {
    'orderId': generateMockData('String')
  },
  response: {
    data: generateMockData('GetOrderBuyerInfoResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrderItemsData = {
  request: {
    'orderId': generateMockData('String'),
  },
  response: {
    data: generateMockData('GetOrderItemsResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrderItemsBuyerInfoData = {
  request: {
    'orderId': generateMockData('String'),
  },
  response: {
    data: generateMockData('GetOrderItemsBuyerInfoResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrderRegulatedInfoData = {
  request: {
    'orderId': generateMockData('String')
  },
  response: {
    data: generateMockData('GetOrderRegulatedInfoResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockgetOrdersData = {
  request: {
    'marketplaceIds': generateMockData('String', true),
  },
  response: {
    data: generateMockData('GetOrdersResponse'),
    statusCode: 200,
    headers: {}
  }
};
const mockupdateVerificationStatusData = {
  request: {
    'orderId': generateMockData('String'),
    'payload': generateMockData('UpdateVerificationStatusRequest')
  },
  response: {
    statusCode: 204,
    headers: {}
  }
};

describe('OrdersV0Api', () => {
  beforeEach(() => {
    sandbox = sinon.createSandbox();
    const apiClientInstance = new SellingPartnerApiForOrders.ApiClient(testEndpoint);
    apiClientInstance.applyXAmzAccessTokenToRequest(testAccessToken);
    sandbox.stub(apiClientInstance, 'callApi');
    instance = new SellingPartnerApiForOrders.OrdersV0Api(apiClientInstance);
  });

  afterEach(() => {
    sandbox.restore();
  });

  describe('confirmShipment', () => {
    it('should successfully call confirmShipment', async () => {
      instance.apiClient.callApi.resolves(mockconfirmShipmentData.response);

      const params = [
        mockconfirmShipmentData.request['orderId'],
        mockconfirmShipmentData.request['payload']
      ];
      const data = await instance.confirmShipment(...params);

      expect(data).to.be.undefined;
    });

    it('should successfully call confirmShipmentWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockconfirmShipmentData.response);

      const params = [
        mockconfirmShipmentData.request['orderId'],
        mockconfirmShipmentData.request['payload']
      ];
      const response = await instance.confirmShipmentWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockconfirmShipmentData.response.statusCode)
      expect(response).to.have.property('headers');
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockconfirmShipmentData.request['orderId'],
          mockconfirmShipmentData.request['payload']
        ];
        await instance.confirmShipment(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrder', () => {
    it('should successfully call getOrder', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderData.response);

      const params = [
        mockgetOrderData.request['orderId']
      ];
      const data = await instance.getOrder(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderResponse).to.be.true;
      expect(data).to.equal(mockgetOrderData.response.data);
    });

    it('should successfully call getOrderWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderData.response);

      const params = [
        mockgetOrderData.request['orderId']
      ];
      const response = await instance.getOrderWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderData.request['orderId']
        ];
        await instance.getOrder(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrderAddress', () => {
    it('should successfully call getOrderAddress', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderAddressData.response);

      const params = [
        mockgetOrderAddressData.request['orderId']
      ];
      const data = await instance.getOrderAddress(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderAddressResponse).to.be.true;
      expect(data).to.equal(mockgetOrderAddressData.response.data);
    });

    it('should successfully call getOrderAddressWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderAddressData.response);

      const params = [
        mockgetOrderAddressData.request['orderId']
      ];
      const response = await instance.getOrderAddressWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderAddressData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderAddressData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderAddressData.request['orderId']
        ];
        await instance.getOrderAddress(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrderBuyerInfo', () => {
    it('should successfully call getOrderBuyerInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderBuyerInfoData.response);

      const params = [
        mockgetOrderBuyerInfoData.request['orderId']
      ];
      const data = await instance.getOrderBuyerInfo(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderBuyerInfoResponse).to.be.true;
      expect(data).to.equal(mockgetOrderBuyerInfoData.response.data);
    });

    it('should successfully call getOrderBuyerInfoWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderBuyerInfoData.response);

      const params = [
        mockgetOrderBuyerInfoData.request['orderId']
      ];
      const response = await instance.getOrderBuyerInfoWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderBuyerInfoData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderBuyerInfoData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderBuyerInfoData.request['orderId']
        ];
        await instance.getOrderBuyerInfo(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrderItems', () => {
    it('should successfully call getOrderItems', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderItemsData.response);

      const params = [
        mockgetOrderItemsData.request['orderId'],
      ];
      const data = await instance.getOrderItems(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderItemsResponse).to.be.true;
      expect(data).to.equal(mockgetOrderItemsData.response.data);
    });

    it('should successfully call getOrderItemsWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderItemsData.response);

      const params = [
        mockgetOrderItemsData.request['orderId'],
      ];
      const response = await instance.getOrderItemsWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderItemsData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderItemsData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderItemsData.request['orderId'],
        ];
        await instance.getOrderItems(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrderItemsBuyerInfo', () => {
    it('should successfully call getOrderItemsBuyerInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderItemsBuyerInfoData.response);

      const params = [
        mockgetOrderItemsBuyerInfoData.request['orderId'],
      ];
      const data = await instance.getOrderItemsBuyerInfo(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderItemsBuyerInfoResponse).to.be.true;
      expect(data).to.equal(mockgetOrderItemsBuyerInfoData.response.data);
    });

    it('should successfully call getOrderItemsBuyerInfoWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderItemsBuyerInfoData.response);

      const params = [
        mockgetOrderItemsBuyerInfoData.request['orderId'],
      ];
      const response = await instance.getOrderItemsBuyerInfoWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderItemsBuyerInfoData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderItemsBuyerInfoData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderItemsBuyerInfoData.request['orderId'],
        ];
        await instance.getOrderItemsBuyerInfo(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrderRegulatedInfo', () => {
    it('should successfully call getOrderRegulatedInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderRegulatedInfoData.response);

      const params = [
        mockgetOrderRegulatedInfoData.request['orderId']
      ];
      const data = await instance.getOrderRegulatedInfo(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrderRegulatedInfoResponse).to.be.true;
      expect(data).to.equal(mockgetOrderRegulatedInfoData.response.data);
    });

    it('should successfully call getOrderRegulatedInfoWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrderRegulatedInfoData.response);

      const params = [
        mockgetOrderRegulatedInfoData.request['orderId']
      ];
      const response = await instance.getOrderRegulatedInfoWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrderRegulatedInfoData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrderRegulatedInfoData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrderRegulatedInfoData.request['orderId']
        ];
        await instance.getOrderRegulatedInfo(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('getOrders', () => {
    it('should successfully call getOrders', async () => {
      instance.apiClient.callApi.resolves(mockgetOrdersData.response);

      const params = [
        mockgetOrdersData.request['marketplaceIds'],
      ];
      const data = await instance.getOrders(...params);

      expect(data instanceof SellingPartnerApiForOrders.GetOrdersResponse).to.be.true;
      expect(data).to.equal(mockgetOrdersData.response.data);
    });

    it('should successfully call getOrdersWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockgetOrdersData.response);

      const params = [
        mockgetOrdersData.request['marketplaceIds'],
      ];
      const response = await instance.getOrdersWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockgetOrdersData.response.statusCode)
      expect(response).to.have.property('headers');
      expect(response).to.have.property('data');
      expect(response.data).to.equal(mockgetOrdersData.response.data)
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockgetOrdersData.request['marketplaceIds'],
        ];
        await instance.getOrders(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });
  describe('updateVerificationStatus', () => {
    it('should successfully call updateVerificationStatus', async () => {
      instance.apiClient.callApi.resolves(mockupdateVerificationStatusData.response);

      const params = [
        mockupdateVerificationStatusData.request['orderId'],
        mockupdateVerificationStatusData.request['payload']
      ];
      const data = await instance.updateVerificationStatus(...params);

      expect(data).to.be.undefined;
    });

    it('should successfully call updateVerificationStatusWithHttpInfo', async () => {
      instance.apiClient.callApi.resolves(mockupdateVerificationStatusData.response);

      const params = [
        mockupdateVerificationStatusData.request['orderId'],
        mockupdateVerificationStatusData.request['payload']
      ];
      const response = await instance.updateVerificationStatusWithHttpInfo(...params);

      expect(response).to.have.property('statusCode');
      expect(response.statusCode).to.equal(mockupdateVerificationStatusData.response.statusCode)
      expect(response).to.have.property('headers');
    });

    it('should handle API errors', async () => {
      const errorResponse = {
        errors: new Error('Expected error to be thrown'),
        statusCode: 400,
        headers: {}
      };
      instance.apiClient.callApi.rejects(errorResponse);

      try {
        const params = [
          mockupdateVerificationStatusData.request['orderId'],
          mockupdateVerificationStatusData.request['payload']
        ];
        await instance.updateVerificationStatus(...params);
        throw new Error('Expected error to be thrown');
      } catch (error) {
        expect(error).to.exist;
        expect(error.statusCode).to.equal(400);
      }
    });
  });

  describe('constructor', () => {
    it('should use default ApiClient when none provided', () => {
      const defaultInstance = new SellingPartnerApiForOrders.OrdersV0Api();
      expect(defaultInstance.apiClient).to.equal(SellingPartnerApiForOrders.ApiClient.instance);
    });

    it('should use provided ApiClient', () => {
      const customClient = new SellingPartnerApiForOrders.ApiClient();
      const customInstance = new SellingPartnerApiForOrders.OrdersV0Api(customClient);
      expect(customInstance.apiClient).to.equal(customClient);
    });
  });
});
